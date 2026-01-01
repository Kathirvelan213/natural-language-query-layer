import { createContext, useState, useContext, useEffect } from "react";
import axios from "axios";

const AuthContext = createContext();
const API_URL = import.meta.env.VITE_API_URL;
const AUTH_URL = import.meta.env.VITE_AUTH_URL;


export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check if user is logged in on mount
    checkAuth();
  }, []);

  const checkAuth = async () => {
    try {
      const response = await axios.get(`${API_URL}auth/user`, {
        withCredentials: true,
      });
      setUser(response.data);
    } catch (err) {
      // If endpoint fails, set as anonymous user
      setUser({ is_authenticated: false });
    } finally {
      setLoading(false);
    }
  };

  const login = () => {
    window.location.href = `${AUTH_URL}auth/login`;
  };

  const logout = async () => {
    try {
      await axios.post(
        `${API_URL}auth/logout`,
        {},
        {
          withCredentials: true,
        }
      );
      // Reload page to clear all state and start fresh
      window.location.href = '/';
    } catch (err) {
      console.error("Logout failed", err);
    }
  };

  return <AuthContext.Provider value={{ user, loading, login, logout, checkAuth }}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within AuthProvider");
  }
  return context;
}
