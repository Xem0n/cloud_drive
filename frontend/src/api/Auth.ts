import { UserInfo } from './types';

const DEFAULT_ERROR = 'Couldn\'t fetch the resources!';

const Fetch = async (url: RequestInfo, init: RequestInit): Promise<object>  => {
    const response = await fetch(url, init);
    const json = await response.json();

    if (!response.ok) {
        throw new Error(json.error || DEFAULT_ERROR);
    }

    return json;
};

const userValidation = async (user: UserInfo) => {
    if (user.username.length < 4 || user.username.length > 80) {
        throw new Error('Provide a valid username (min. 4 characters and max. 80 characters)!');
    }

    if (user.password.length < 8 || user.password.length > 16) {
        throw new Error('Provide a valid password (min. 8 characters and max. 16 characters)!');
    }
}

const login = async (user: UserInfo) => {
    await userValidation(user);

    // todo fetch
};

const register = async (user: UserInfo) => {
    await userValidation(user);

    if (user.confirmedPassword === undefined) {
        throw new Error('Confirm the password!');
    }

    if (user.password !== user.confirmedPassword) {
        throw new Error('Passwords don\'t match!');
    }

    // todo fetch
};

export { login, register };