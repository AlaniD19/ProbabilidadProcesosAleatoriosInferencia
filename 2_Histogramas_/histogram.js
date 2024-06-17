document.getElementById('file').addEventListener('change', handleFileSelect, false);

function handleFileSelect(event) {
  const file = event.target.files[0];
  if (file && file.name === "random_numbers.txt") {
    const reader = new FileReader();
    reader.onload = function(e) {
      const text = e.target.result;
      const numbers = text.split(' ').map(Number);
      const frequencies = countFrequencies(numbers);
      createHistogram(frequencies);
    };
    reader.readAsText(file);
  } else {
    alert("Por favor selecciona el archivo correcto (random_numbers.txt)");
  }
}

function countFrequencies(numbers) {
  const frequencyMap = new Map();
  numbers.forEach(num => {
    frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
  });
  return Array.from(frequencyMap.entries()).sort((a, b) => a[0] - b[0]);
}

function createHistogram(frequencies) {
  const ctx = document.getElementById('myChart').getContext('2d');
  const labels = frequencies.map(entry => entry[0]);
  const data = frequencies.map(entry => entry[1]);

  // Datos del histograma
  const chartData = {
    labels: labels, // Etiquetas para cada barra (1-6)
    datasets: [{
      label: 'Frecuencia',
      data: data, // Datos de las barras
      backgroundColor: 'rgba(75, 192, 192, 0.2)', // Color de las barras
      borderColor: 'rgba(75, 192, 192, 1)', // Color del borde de las barras
      borderWidth: 1
    }]
  };

  // Configuración del histograma
  const config = {
    type: 'bar',
    data: chartData,
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  };

  // Crear el gráfico
  new Chart(ctx, config);
}
