const cards = document.getElementById('cards')
const items = document.getElementById('items')
const footer = document.getElementById('footer')
const templateCard = document.getElementById('template-card').content
const templateFooter = document.getElementById('template-footer').content
const templateCarrito = document.getElementById('template-carrito').content
const fragment = document.createDocumentFragment()
let carrito = {}
   



//DOMContentLoaded, es al cargar la pagina y objetos
document.addEventListener('DOMContentLoaded',() => { 
    fetchData()
    //carrito es llave inventada
    if(localStorage.getItem('carrito')){
        carrito = JSON.parse(localStorage.getItem('carrito'))
        pintarCarrito()
    }
})
cards.addEventListener('click',e =>{
    addCarrito(e) /* Permite capturar el elemento clickeado en pantalla*/
})

items.addEventListener('click',e=>{
    btnAccion(e)
})








const fetchData = async() =>{
    try {
        const res = await fetch('/api/lista_productos')
        const data = await res.json()
        pintarCards(data)
    } catch (error) {
        console.log(error)
    }
}

const pintarCards = data =>{
    data.forEach(producto =>{
        templateCard.querySelector('h5').textContent = producto.nombre
        templateCard.querySelector('h4').textContent = producto.precio
        templateCard.querySelector('p').textContent = producto.stock
        templateCard.querySelector('img').setAttribute("src",producto.image)
        templateCard.querySelector('.btn-dark').dataset.id = producto.idProd
        const clone = templateCard.cloneNode(true)
        fragment.appendChild(clone)
    })
    cards.appendChild(fragment)
}


const addCarrito = e =>{
    //console.log(e.target)
    //console.log(e.target.classList.contains('btn-dark')) /*Manda true o false, si el elemento clickeado contiene la clase mencionada*/
    if(e.target.classList.contains('btn-dark')){
        setCarrito(e.target.parentElement) //Empuja todo el div o elemento seleccionado en boton Comprar, a setcarrito
    }
    e.stopPropagation()
}

const setCarrito = objeto =>{
    const producto = {
        idProd: objeto.querySelector('.btn-dark').dataset.id, //Ahora el objeto traido de AddCarrito, solo captura el id creado para cada boton 
        nombre: objeto.querySelector('h5').textContent,
        precio : objeto.querySelector('h4').textContent,
        cantidad: 1
        
    }
    if (carrito.hasOwnProperty(producto.idProd)){
        producto.cantidad = carrito[producto.idProd].cantidad +1 

    }

    carrito[producto.idProd]= {...producto} //3 puntitos adquiere, Copia , de producto
    pintarCarrito()

}


const pintarCarrito = () =>{
    //console.log(carrito)
    items.innerHTML='' //Hace que empiece vacio el items, por lo cual no se repiten los productos en carrito
    Object.values(carrito).forEach(producto =>{
        templateCarrito.querySelector('th').textContent = producto.idProd
        templateCarrito.querySelectorAll('td')[0].textContent = producto.nombre
        templateCarrito.querySelectorAll('td')[1].textContent = producto.cantidad
        templateCarrito.querySelector('.btn-info').dataset.id = producto.idProd
        templateCarrito.querySelector('.btn-danger').dataset.id = producto.idProd
        templateCarrito.querySelector('span').textContent= producto.cantidad * producto.precio



       

        const clone = templateCarrito.cloneNode(true)
        fragment.appendChild(clone)
    })
    items.appendChild(fragment)

    pintarFooter()

    localStorage.setItem('carrito',JSON.stringify(carrito))
}




const pintarFooter = () =>{
    footer.innerHTML=''
    if(Object.keys(carrito).length === 0){
        footer.innerHTML= '<th scope="row" colspan="5">Carrito vacío - comience a comprar!</th>'
        return
    }
    
    const nCantidad = Object.values(carrito).reduce((acc,{cantidad})=>acc + cantidad,0)
    const nPrecio = Object.values(carrito).reduce((acc,{cantidad,precio}) => acc+cantidad*precio,0)


     

    templateFooter.querySelectorAll('td')[0].textContent = nCantidad
    templateFooter.querySelector('span').textContent = nPrecio
       
  
    

    


    const clone = templateFooter.cloneNode(true)
    fragment.appendChild(clone)
    footer.appendChild(fragment)

    const btnVaciar = document.getElementById('vaciar-carrito')
    btnVaciar.addEventListener('click',()=>{
        carrito = {}
        pintarCarrito()
    })

  
}

const btnAccion = e =>{
    //accion de aumentar con boton
    if(e.target.classList.contains('btn-info')){      
        const producto =  carrito[e.target.dataset.id]
        producto.cantidad =  carrito[e.target.dataset.id].cantidad + 1 // = ++
        carrito[e.target.dataset.id] = {...producto}
        pintarCarrito()
    }
    //accion de disminuir con boton
    if(e.target.classList.contains('btn-danger')){
        const producto =  carrito[e.target.dataset.id]
        producto.cantidad =  carrito[e.target.dataset.id].cantidad - 1
        if(producto.cantidad === 0){
            delete  carrito[e.target.dataset.id]
        }
        pintarCarrito()
    }
    e.stopPropagation()
}



