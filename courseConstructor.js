class Car {
    // initialize the car instances
    constructor(make, model, year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }
    getMake() {
        return this.make;
    }
    getModel() {
        return this.model;
    }
    getYear() {
        return this.year;
    }
    getInfo() {
        return `${this.make} ${this.model} ${this.year}`;
    }

    turboOn() {
        console.log("Turbo is on!");
    }
}

let car1 = new Car("Toyota", "Camry", 2020); // car objects

console.log(car1.getInfo());
// car1 is the object
// turboOn() is the method
car1.turboOn(); // I don't have to console.log this because it's done within the method.