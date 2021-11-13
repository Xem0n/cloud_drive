import React, { useEffect } from 'react';
import Router from './Router';
import Token from 'api/Token';
import { useLocation, useNavigate } from 'react-router';

const FORM_PATHS = [
  '/login',
  '/register'
];

const App = () => {
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    if (Token.get() !== '') {
      return;
    }

    if (FORM_PATHS.includes(location.pathname)) {
      return;
    }

    navigate('/login');
  }, [navigate, location]);

  return (
    <div className="App">
      <Router />
    </div>
  );
};

export default App;