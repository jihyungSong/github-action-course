
export class Human {

    private name: string;
    private age: number;

    constructor(name: string) {
        this.name = name;
        this.age = 20;
    }

    public GetName(): string {
        return this.name;
    }

    public SetName(name: string): void {
        this.name = name;
    }

    public GetAge(): number {
        return this.age;
    }

    public SetAge(age: number): void {
        this.age = age;
    }
    
    public GetInfo(): string {
        return `My name is ${this.name} and ${this.age} years old.`;
    }
}
