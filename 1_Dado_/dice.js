document.getElementById("cube").addEventListener('click', function() {
    var dado = document.getElementById("cube")
    var data = document.getElementById("number_faces")
    if(data.value != "") {
        var number = document.getElementById("random_number")
        number.style.opacity = 0
        setTimeout(function() {
            var random = random_gen(data.value)
            number.textContent = random
            dado.classList.remove("animate")
            void dado.offsetWidth
            dado.classList.add("animate")
            setTimeout(function() {
                number.style.opacity = 1
            }, 3000)
        }, 300)
    } else {
        alert("ERROR: Debes asignar el número de lados del dado")
    }
})

document.getElementById("test100k").addEventListener('click', function() {
    test_100k()
})

// Función para generar una nueva semilla basada en el tiempo actual
function generateSeed() {
    return new Date().getTime();
}
/**
 * Generador Lineal Congruente (LCG)
 * 
 * Fórmula:
 * X_{n+1} = (a * X_n + c) % m
 * 
 * Donde:
 * - X es la secuencia de números pseudoaleatorios.
 * - a es el multiplicador.
 * - c es el incremento.
 * - m es el módulo.
 * - X_0 es la semilla o valor inicial.
 * 
 * Parámetros comunes:
 * - a = 1664525
 * - c = 1013904223
 * - m = 2^32 (4294967296)
 * 
 * Esta configuración de parámetros es ampliamente utilizada y proporciona una buena calidad de números pseudoaleatorios.
 * 
 * @param {number} seed - La semilla inicial para el generador.
 * @returns {number} - Un nuevo número pseudoaleatorio basado en la semilla.
 */
function lcg(seed) {
    const a = 1664525; // El multiplicador
    const c = 1013904223; // El incremento
    const m = 2 ** 32; // El módulo (2^32 para obtener números de 32 bits)
    return (a * seed + c) % m; // Fórmula LCG para calcular el siguiente número en la secuencia
}
// Función para generar un número aleatorio en el rango 0 a n
function random_gen(n) {
    let seed = generateSeed(); // Genera una nueva semilla cada vez que se llama a la función
    seed = lcg(seed); // Calcula la siguiente semilla en la secuencia pseudoaleatoria
    const randomNumber = (seed % n)+1; // Ajusta el número al rango 1 a n
    return randomNumber;
}

// test 100k veces
// Función para generar y descargar números aleatorios
function test_100k() {
    let results = [];
    seed = generateSeed()

    for (let i = 0; i < 100000; i++) {
        seed = lcg(seed);
        let randomNumber = (seed % 6)+1;
        results.push(randomNumber);
    }

    // Convertir el array de números a una cadena de texto separada por espacios
    let data = results.join(' ');

    // Crear un Blob con los datos
    let blob = new Blob([data], { type: 'text/plain' });
    let url = URL.createObjectURL(blob);

    // Crear un enlace para descargar el archivo
    let a = document.createElement('a');
    a.href = url;
    a.download = 'random_numbers.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}