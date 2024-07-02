// functional programming
// Object-oriented programming is easier to write and easier to understand
const shoes = 100
const stateTax = .05

function totalPrice(shoes, stateTax) {
    let totalTax = shoes * stateTax
    let shoeTotal = totalTax + shoes
    return { totalTax, shoeTotal } // Syntax for returning multiple values
}

// Call the function and store result in a variable
const result = totalPrice(shoes, stateTax)
// Console log total tax and total price by calling the result variable (above  )
console.log(`Total Tax = $${result.totalTax}\nTotal Price = $${result.shoeTotal}`)