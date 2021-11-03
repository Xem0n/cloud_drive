import React, { useEffect } from 'react';
import Router from './Router';
import Token from 'api/Token';
import { useNavigate } from 'react-router';

const App = () => {
  const navigate = useNavigate();

  useEffect(() => {
    if (Token.get() === '') {
      navigate('/login');
    }
  }, [navigate]);

  return (
    <div className="App">
      <Router />
    </div>
  );
};

export default App;