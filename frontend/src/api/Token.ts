class Token {
    private static token = '';

    static get(): string {
        if (this.token === '') {
            this.getFromLocalStorage();
        }

        return this.token;
    }

    private static getFromLocalStorage(): void {
        this.token = localStorage.getItem('token') || '';
    }

    static set(newToken: string): void {
        this.token = newToken;
        localStorage.setItem('token', newToken);
    }
}

export default Token;