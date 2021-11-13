import { Routes, Route } from 'react-router-dom';
import Form, { FormTypes } from './Form';

const Router = () => (
    <Routes>
        <Route path='/' element={<h1>main page</h1>} />
        <Route path='login' element={<Form type={FormTypes.Login} />} />
        <Route path='register' element={<Form type={FormTypes.Register} />} />
    </Routes>
);

export default Router;