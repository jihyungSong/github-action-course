
class Cat {

    constructor(name) {
        this.name = name;
        this.status = 'normal';
    }

    GetName(){
        return this.name;
    }

    SetName(name){
        this.name = name;
    }

    GetStatus(){
        return this.status;
    }

    SetStatus(status) {
        if (status !== 'normal' && status !== 'sleepy' && status !== 'hungry' && status !== 'angry') {
            throw new Error('Not allowed status');
        }
        this.status = status;
    }

    Meow() {
        return 'Meow~';
    }
}

module.exports = Cat;
