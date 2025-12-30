import { useAuth } from "../../context/AuthContext";
import "./styles/loginButton.css";

export function LoginButton() {
  const { user, login, logout } = useAuth();

  const handleLogin = () => {
    console.log("Login clicked, redirecting to http://localhost:8000/auth/login");
    login();
  };

  if (user) {
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
