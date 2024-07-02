// Object-oriented programming
// Notice how everything is a property of an object and done within the object.
let purchase1 = {
    shoes: 100,
    stateTax: .05,
    totalPrice: function() {
        let totalTax = purchase1.shoes * purchase1.stateTax
        // Makes sure \n uses forward slashes for paragraph breaks
        console.log("First Purchase")
        console.log(`Shoe Cost = $${purchase1.shoes}\nTotal Tax = $${totalTax}\nTotal Price = $${purchase1.shoes + totalTax}`)
    }
}

// I can create as many objects as I want that follows the same pattern
let purchase2 = {
    shoes: 60,
    stateTax:.05,
    totalPrice: function() {
        // I can also use this.shoes and this.stateTax instead of purchase1.shoes and purchase1.stateTax
        // "this" means this object. Cuts down on time because I can copy from the first object
        let totalTax = this.shoes * this.stateTax
        console.log("Second Purchase")
        console.log(`Shoe Cost = $${purchase2.shoes}\nTotal Tax = $${totalTax}\nTotal Price = $${purchase2.shoes + totalTax}`)
    }
}
// Then I can call the function on each object (see below)

// Always have to call the function so...
// Call the object (i.e., purchase1) with the function (i.e., totalPrice)
purchase1.totalPrice()
console.log() // Adds a blank line between each purchase
purchase2.totalPrice()