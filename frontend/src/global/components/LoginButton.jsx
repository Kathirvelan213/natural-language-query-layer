import { useAuth } from "../../context/AuthContext";
import "./styles/loginButton.css";

export function LoginButton() {
  const { user, loading, login, logout } = useAuth();

  const handleLogin = () => {
    login();
  };

  if (loading) {
    return null;
  }

  if (user?.is_authenticated) {
    return (
      <button className="login-button logout" onClick={logout}>
        Logout
      </button>
    );
  }

  return (
    <button className="login-button" onClick={handleLogin}>
      Login with Google
    </button>
  );
}
