import { useLocation } from 'react-router';
import { Routes, Route } from 'react-router-dom';
import { TransitionGroup, CSSTransition } from 'react-transition-group';
import Form, { FormTypes } from './Form';
import './Router.css';

// todo
// add conditional transition
// and fix overriding (?) forms

const Router = () => {
    const location = useLocation();

    return (
        <TransitionGroup component={null}>
            <CSSTransition
                key={location.key}
                timeout={400}
                classNames={'route'}>
                <Routes>
                    <Route path='/' element={<h1>main page</h1>} />
                    <Route path='login' element={<Form type={FormTypes.Login} />} />
                    <Route path='register' element={<Form type={FormTypes.Register} />} />
                </Routes>
            </CSSTransition>
        </TransitionGroup>
    );
};

export default Router;