let products =[
    {name : "mobile",
    cost:"10000"},
    {name:"ipad",
    cost:"65000"},
    {name:"laptop",
    cost:"70000"}
]



function getProducts(){
    setTimeout(()=>{
        let result = '';
        products.forEach((product,index)=>{
            result += `<li>${product.name}</li>`

})
    document.body.innerHTML = result

},2000)

}
getProducts();
function createProducts(product,callback) {
    setTimeout(()=>{
        products.push(product)
        callback();
    },2000)

}
// function createProducts(product) {
// return new Promise((reslove,reject)=>{
// setTimeout(()=>{
// products.push(product);
// let error =false
// if(!error){
//     reslove();
// }
// else{
//     reject("Error:error from database")
// }
// },1000)
// })


// }

// createProducts({name:"washing machine",cost:"200"}).than(getProducts).catch(err=>console.log(err));