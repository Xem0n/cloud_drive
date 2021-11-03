import { Routes, Route } from 'react-router-dom';

const Router = () => (
    <Routes>
        <Route path='/' element={<h1>main page</h1>} />
        <Route path='login' element={<h1>login</h1>} />
    </Routes>
);

export default Router;