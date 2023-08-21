
export class Human {

    private name: string;
    private status: string;

    constructor(name: string) {
        this.name = name;
        this.status = 'normal';
    }

    public GetName(): string {
        return this.name;
    }

    public SetName(name: string): void {
        this.name = name;
    }

    public GetStatus(): string {
        return this.status;
    }

    public SetStatus(status: string): void {
        if (status !== 'normal' && status !== 'sleepy' && status !== 'hungry' && status !== 'angry') {
            throw new Error('Not allowed status');
        }
        this.status = status;
    }

    public Meow(): string {
        return 'Meow~';
    }
}
