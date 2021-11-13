import { FormEvent, useState } from 'react';
import { Link } from 'react-router-dom';
import Text from './inputs/Text';
import Submit from './inputs/Submit';
import './Form.css';

enum FormTypes {
    Login,
    Register
};

const FormInfo = {
    // Login
    0: {
        submit: 'Log In',
        link: '/register',
        linkText: 'Create new account'
    },
    // Register
    1: {
        submit: 'Register',
        link: '/login',
        linkText: 'Already have an account? Log In'
    }
};

type FormProps = {
    type: FormTypes;
};

const Form = (props: FormProps) => {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');

    const info = FormInfo[props.type];

    const submit = (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();
    };

    return (
        <form className='form' onSubmit={submit}>
            <Text
                name='name'
                type='text'
                value={email}
                onChange={setEmail}
                placeholder='Username' />

            <Text
                name='password'
                type='password'
                value={password}
                onChange={setPassword}
                placeholder='Password' />

            {props.type === FormTypes.Register &&
                <Text 
                    name='confirmPassword'
                    type='password'
                    value={confirmPassword}
                    onChange={setConfirmPassword}
                    placeholder='Confirm password' />
            }

            <Submit value={info.submit} />

            <Link 
                className='form-link'
                to={info.link}>
                {info.linkText}
            </Link>
        </form>
    );
};

export { Form as default, FormTypes };