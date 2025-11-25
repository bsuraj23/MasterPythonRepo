import React, { useState, useEffect } from 'react';

const App = () => {
    const [backendMessage, setBackendMessage] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const [status, setStatus] = useState('');
    const [user, setUser] = useState(null);
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [loginForm, setLoginForm] = useState({ username: '', password: '' });
    const [sessions, setSessions] = useState(null);
    const [googleAuthUrl, setGoogleAuthUrl] = useState(null);
    const [googleConfigured, setGoogleConfigured] = useState(false);

    // Fetch with credentials to include cookies
    const fetchWithCredentials = async (url, options = {}) => {
        return fetch(url, {
            ...options,
            credentials: 'include', // Important for cookies
            headers: {
                'Content-Type': 'application/json',
                ...options.headers,
            },
        });
    };

    const checkAuthentication = async () => {
        try {
            const response = await fetchWithCredentials('http://localhost:8000/api/me');
            if (response.ok) {
                const userData = await response.json();
                setUser(userData);
                setIsAuthenticated(true);
            } else {
                setUser(null);
                setIsAuthenticated(false);
            }
        } catch (err) {
            setUser(null);
            setIsAuthenticated(false);``
        }
    };

    const checkGoogleAuth = async () => {
        try {
            const response = await fetchWithCredentials('http://localhost:8000/auth/google/url');
            if (response.ok) {
                const data = await response.json();
                setGoogleAuthUrl(data.google_auth_url);
                setGoogleConfigured(data.configured);
            }
        } catch (err) {
            setGoogleConfigured(false);
        }
    };

    const handleGoogleLogin = () => {
        if (googleAuthUrl) {
            window.location.href = googleAuthUrl;
        }
    };

    // Check for authentication status from URL parameters (after Google OAuth redirect)
    const checkUrlParams = () => {
        const urlParams = new URLSearchParams(window.location.search);
        const authStatus = urlParams.get('auth');
        const message = urlParams.get('message');

        if (authStatus === 'success') {
            setStatus('Google OAuth login successful!');
            checkAuthentication(); // Refresh user data
            // Clean up URL
            window.history.replaceState({}, document.title, window.location.pathname);
        } else if (authStatus === 'error') {
            setError(`Google OAuth error: ${message || 'Unknown error'}`);
            // Clean up URL
            window.history.replaceState({}, document.title, window.location.pathname);
        }
    };

    const handleLogin = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');
        
        try {
            const response = await fetchWithCredentials('http://localhost:8000/api/login', {
                method: 'POST',
                body: JSON.stringify(loginForm),
            });

            if (response.ok) {
                const data = await response.json();
                setUser(data.user);
                setIsAuthenticated(true);
                setLoginForm({ username: '', password: '' });
                setStatus('Login successful! Session cookie set.');
                fetchStatus(); // Refresh status
            } else {
                const errorData = await response.json();
                setError(errorData.detail || 'Login failed');
            }
        } catch (err) {
            setError(`Login failed: ${err.message}`);
        } finally {
            setLoading(false);
        }
    };

    const handleLogout = async () => {
        setLoading(true);
        try {
            const response = await fetchWithCredentials('http://localhost:8000/api/logout', {
                method: 'POST',
            });

            if (response.ok) {
                setUser(null);
                setIsAuthenticated(false);
                setBackendMessage('');
                setStatus('Logout successful! Session cookie cleared.');
                setSessions(null);
                fetchStatus(); // Refresh status
            }
        } catch (err) {
            setError(`Logout failed: ${err.message}`);
        } finally {
            setLoading(false);
        }
    };

    const fetchHelloFromBackend = async () => {
        setLoading(true);
        setError('');
        try {
            const response = await fetchWithCredentials('http://localhost:8000/api/hello');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            setBackendMessage(data.message);
            setStatus('Successfully fetched data from backend!');
        } catch (err) {
            setError(`Failed to connect to backend: ${err.message}`);
            setBackendMessage('');
        } finally {
            setLoading(false);
        }
    };

    const fetchStatus = async () => {
        try {
            const response = await fetchWithCredentials('http://localhost:8000/api/status');
            if (response.ok) {
                const data = await response.json();
                setStatus(`Backend Status: ${data.status} - ${data.message} (Auth: ${data.authenticated ? 'Yes' : 'No'})`);
            }
        } catch (err) {
            setStatus('Backend not connected');
        }
    };

    const fetchSessions = async () => {
        try {
            const response = await fetchWithCredentials('http://localhost:8000/api/sessions');
            if (response.ok) {
                const data = await response.json();
                setSessions(data);
            } else {
                setSessions(null);
            }
        } catch (err) {
            setSessions(null);
        }
    };

    useEffect(() => {
        const initializeApp = async () => {
            checkUrlParams(); // Check for OAuth callback parameters
            await checkAuthentication();
            await fetchStatus();
            await checkGoogleAuth();
        };
        initializeApp();
    }, []); // eslint-disable-line react-hooks/exhaustive-deps

    return (
        <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif', maxWidth: '1200px', margin: '0 auto' }}>
            <h1>🍪 React + FastAPI with Cookies & Authentication</h1>
            
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px', marginBottom: '20px' }}>
                {/* Frontend Status */}
                <div style={{ padding: '15px', backgroundColor: '#f0f0f0', borderRadius: '8px' }}>
                    <h2>🌐 Frontend (React)</h2>
                    <p>✅ React app running on http://localhost:3000</p>
                    <p>🍪 Cookies: Enabled with credentials</p>
                </div>

                {/* Backend Status */}
                <div style={{ padding: '15px', backgroundColor: '#e8f5e8', borderRadius: '8px' }}>
                    <h2>⚡ Backend Status</h2>
                    <p>{status || 'Checking backend connection...'}</p>
                </div>
            </div>

            {/* Authentication Section */}
            <div style={{ marginBottom: '20px', padding: '20px', backgroundColor: '#fff3cd', borderRadius: '8px' }}>
                <h2>🔐 Authentication Status</h2>
                
                {isAuthenticated ? (
                    <div>
                        <p>✅ <strong>Logged in as:</strong> {user?.full_name} ({user?.username})</p>
                        <p>📧 <strong>Email:</strong> {user?.email}</p>
                        <p>🔐 <strong>Auth Provider:</strong> {user?.auth_provider === 'google' ? 'Google OAuth' : 'Local Account'}</p>
                        <button 
                            onClick={handleLogout}
                            disabled={loading}
                            style={{
                                padding: '10px 20px',
                                fontSize: '16px',
                                backgroundColor: '#dc3545',
                                color: 'white',
                                border: 'none',
                                borderRadius: '5px',
                                cursor: loading ? 'not-allowed' : 'pointer',
                                marginRight: '10px'
                            }}
                        >
                            {loading ? 'Logging out...' : 'Logout'}
                        </button>
                        <button 
                            onClick={fetchSessions}
                            style={{
                                padding: '10px 20px',
                                fontSize: '16px',
                                backgroundColor: '#17a2b8',
                                color: 'white',
                                border: 'none',
                                borderRadius: '5px',
                                cursor: 'pointer'
                            }}
                        >
                            View Sessions
                        </button>
                    </div>
                ) : (
                    <div>
                        <p>❌ <strong>Not logged in</strong></p>
                        
                        {/* Google OAuth Login */}
                        {googleConfigured && (
                            <div style={{ marginBottom: '20px', padding: '15px', backgroundColor: '#f8f9fa', borderRadius: '8px' }}>
                                <h4>🚀 Login with Google OAuth</h4>
                                <button 
                                    onClick={handleGoogleLogin}
                                    style={{
                                        padding: '12px 24px',
                                        fontSize: '16px',
                                        backgroundColor: '#4285f4',
                                        color: 'white',
                                        border: 'none',
                                        borderRadius: '5px',
                                        cursor: 'pointer',
                                        display: 'flex',
                                        alignItems: 'center',
                                        gap: '8px'
                                    }}
                                >
                                    <span>🔍</span> Sign in with Google
                                </button>
                                <p style={{ fontSize: '12px', color: '#666', marginTop: '8px' }}>
                                    Secure OAuth login using your Google account
                                </p>
                            </div>
                        )}

                        {/* Traditional Login Form */}
                        <div style={{ padding: '15px', backgroundColor: '#f0f0f0', borderRadius: '8px' }}>
                            <h4>📝 Or login with username/password</h4>
                            <form onSubmit={handleLogin} style={{ marginTop: '15px' }}>
                                <div style={{ marginBottom: '10px' }}>
                                    <input
                                        type="text"
                                        placeholder="Username (try: testuser)"
                                        value={loginForm.username}
                                        onChange={(e) => setLoginForm({...loginForm, username: e.target.value})}
                                        style={{ padding: '8px', marginRight: '10px', borderRadius: '4px', border: '1px solid #ccc' }}
                                        required
                                    />
                                    <input
                                        type="password"
                                        placeholder="Password (try: testpass123)"
                                        value={loginForm.password}
                                        onChange={(e) => setLoginForm({...loginForm, password: e.target.value})}
                                        style={{ padding: '8px', marginRight: '10px', borderRadius: '4px', border: '1px solid #ccc' }}
                                        required
                                    />
                                    <button 
                                        type="submit"
                                        disabled={loading}
                                        style={{
                                            padding: '8px 15px',
                                            backgroundColor: '#28a745',
                                            color: 'white',
                                            border: 'none',
                                            borderRadius: '4px',
                                            cursor: loading ? 'not-allowed' : 'pointer'
                                        }}
                                    >
                                        {loading ? 'Logging in...' : 'Login'}
                                    </button>
                                </div>
                            </form>
                            <p style={{ fontSize: '14px', color: '#666' }}>
                                Demo credentials: username=<code>testuser</code>, password=<code>testpass123</code>
                            </p>
                        </div>
                    </div>
                )}
            </div>

            {/* API Testing */}
            <div style={{ marginBottom: '20px' }}>
                <button 
                    onClick={fetchHelloFromBackend} 
                    disabled={loading}
                    style={{
                        padding: '12px 24px',
                        fontSize: '16px',
                        backgroundColor: '#007bff',
                        color: 'white',
                        border: 'none',
                        borderRadius: '5px',
                        cursor: loading ? 'not-allowed' : 'pointer'
                    }}
                >
                    {loading ? 'Loading...' : '🍪 Get Hello from FastAPI (with cookies)'}
                </button>
            </div>

            {/* Backend Response */}
            {backendMessage && (
                <div style={{ 
                    padding: '15px', 
                    backgroundColor: '#d4edda', 
                    border: '1px solid #c3e6cb',
                    borderRadius: '5px',
                    marginBottom: '20px'
                }}>
                    <h3>✅ Backend Response</h3>
                    <p><strong>Message:</strong> {backendMessage}</p>
                    <p><em>This response includes your authentication status via cookies!</em></p>
                </div>
            )}

            {/* Sessions Info */}
            {sessions && (
                <div style={{ 
                    padding: '15px', 
                    backgroundColor: '#e2e3e5', 
                    border: '1px solid #d6d8db',
                    borderRadius: '5px',
                    marginBottom: '20px'
                }}>
                    <h3>🔗 Active Sessions</h3>
                    <p><strong>Total Sessions:</strong> {sessions.total_sessions}</p>
                    {sessions.sessions.map((session, index) => (
                        <div key={index} style={{ margin: '5px 0', padding: '5px', backgroundColor: '#f8f9fa', borderRadius: '3px' }}>
                            <small>User: {session.username} | ID: {session.session_id} | Created: {new Date(session.created_at).toLocaleString()}</small>
                        </div>
                    ))}
                </div>
            )}

            {/* Error Display */}
            {error && (
                <div style={{ 
                    padding: '15px', 
                    backgroundColor: '#f8d7da', 
                    border: '1px solid #f5c6cb',
                    borderRadius: '5px',
                    marginBottom: '20px'
                }}>
                    <h3>❌ Error</h3>
                    <p>{error}</p>
                </div>
            )}

            {/* Features Overview */}
            <div style={{ marginTop: '30px', padding: '20px', backgroundColor: '#e7f3ff', borderRadius: '8px' }}>
                <h3>🚀 Authentication Features Implemented</h3>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '15px' }}>
                    <div>
                        <h4>✅ Backend Features</h4>
                        <ul>
                            <li>🍪 Secure HTTP-only cookies</li>
                            <li>🔐 JWT-based sessions</li>
                            <li>👤 Local user authentication</li>
                            <li>� Google OAuth 2.0 integration</li>
                            <li>�🛡️ CORS with credentials</li>
                            <li>⏰ Session expiration</li>
                            <li>🔄 Multiple auth providers</li>
                        </ul>
                    </div>
                    <div>
                        <h4>✅ Frontend Features</h4>
                        <ul>
                            <li>🍪 Automatic cookie handling</li>
                            <li>🔐 Dual login options</li>
                            <li>🔍 Google OAuth button</li>
                            <li>👤 User state management</li>
                            <li>🔄 Session persistence</li>
                            <li>📊 Session monitoring</li>
                            <li>🎨 Modern UI/UX</li>
                        </ul>
                    </div>
                </div>
            </div>

            {/* Next Steps */}
            <div style={{ marginTop: '20px', padding: '15px', backgroundColor: '#fff3cd', borderRadius: '5px' }}>
                <h3>🔮 Next Steps</h3>
                <ul>
                    <li>✅ Cookie-based authentication</li>
                    <li>✅ Google OAuth integration</li>
                    <li>📋 Setup Google OAuth credentials</li>
                    <li>🔄 Add database integration</li>
                    <li>🛡️ Add password hashing</li>
                    <li>👤 User registration</li>
                    <li>🔒 Protected routes</li>
                    <li>📱 Responsive design</li>
                </ul>
            </div>
        </div>
    );
};

export default App;