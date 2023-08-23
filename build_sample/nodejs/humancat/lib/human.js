
class Human {

    constructor(name) {
        this.name = name;
        this.age = 20;
    }

    GetName() {
        return this.name;
    }

    SetName(name) {
        this.name = name;
    }

    GetAge() {
        return this.age;
    }

    SetAge(age) {
        this.age = age;
    }
    
    GetInfo() {
        return `My name is ${this.name} and ${this.age} years old.`;
    }
}

module.exports = Human;
