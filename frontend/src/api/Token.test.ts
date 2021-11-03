import Token from './Token';

test('updates token value', () => {
    const newValue = 'random value';

    Token.set(newValue);
    expect(Token.get()).toBe(newValue);
});