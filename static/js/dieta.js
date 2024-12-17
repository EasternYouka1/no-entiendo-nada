document.addEventListener('DOMContentLoaded', function() {
    var predefinedData = {
    'Manzana': {'tipo_comida': 'desayuno', 'calorias': 52, 'carbohidratos': 14, 'proteinas': 0, 'grasas': 0},
    'Pollo': {'tipo_comida': 'almuerzo', 'calorias': 239, 'carbohidratos': 0, 'proteinas': 27, 'grasas': 14},
    'Avena': {'tipo_comida': 'desayuno', 'calorias': 150, 'carbohidratos': 27, 'proteinas': 5, 'grasas': 3},
    'Tostada con aguacate': {'tipo_comida': 'desayuno', 'calorias': 250, 'carbohidratos': 30, 'proteinas': 6, 'grasas': 12},
    'Ensalada César': {'tipo_comida': 'almuerzo', 'calorias': 300, 'carbohidratos': 10, 'proteinas': 20, 'grasas': 20},
    'Sopa de lentejas': {'tipo_comida': 'almuerzo', 'calorias': 180, 'carbohidratos': 30, 'proteinas': 12, 'grasas': 4},
    'Pasta con salsa de tomate': {'tipo_comida': 'almuerzo', 'calorias': 350, 'carbohidratos': 60, 'proteinas': 10, 'grasas': 8},
    'Pizza Margarita': {'tipo_comida': 'cena', 'calorias': 300, 'carbohidratos': 40, 'proteinas': 12, 'grasas': 10},
    'Sándwich de jamón y queso': {'tipo_comida': 'almuerzo', 'calorias': 250, 'carbohidratos': 30, 'proteinas': 15, 'grasas': 10},
    'Yogur con frutas': {'tipo_comida': 'desayuno', 'calorias': 200, 'carbohidratos': 30, 'proteinas': 8, 'grasas': 5},
    'Batido de proteínas': {'tipo_comida': 'snack', 'calorias': 150, 'carbohidratos': 10, 'proteinas': 20, 'grasas': 2},
    'Ensalada de quinoa': {'tipo_comida': 'almuerzo', 'calorias': 220, 'carbohidratos': 35, 'proteinas': 8, 'grasas': 6},
    'Tacos de pollo': {'tipo_comida': 'cena', 'calorias': 300, 'carbohidratos': 40, 'proteinas': 20, 'grasas': 10},
    'Burrito de carne': {'tipo_comida': 'almuerzo', 'calorias': 400, 'carbohidratos': 50, 'proteinas': 20, 'grasas': 15},
    'Panqueques con miel': {'tipo_comida': 'desayuno', 'calorias': 350, 'carbohidratos': 60, 'proteinas': 8, 'grasas': 10},
    'Filete de salmón': {'tipo_comida': 'cena', 'calorias': 350, 'carbohidratos': 0, 'proteinas': 30, 'grasas': 20},
    'Ensalada de atún': {'tipo_comida': 'almuerzo', 'calorias': 250, 'carbohidratos': 10, 'proteinas': 20, 'grasas': 15},
    'Wrap de pollo': {'tipo_comida': 'almuerzo', 'calorias': 300, 'carbohidratos': 40, 'proteinas': 20, 'grasas': 10},
    'Bowl de acai': {'tipo_comida': 'desayuno', 'calorias': 200, 'carbohidratos': 40, 'proteinas': 5, 'grasas': 5},
    'Galletas de avena': {'tipo_comida': 'snack', 'calorias': 150, 'carbohidratos': 20, 'proteinas': 3, 'grasas': 6},
    'Helado de vainilla': {'tipo_comida': 'snack', 'calorias': 200, 'carbohidratos': 25, 'proteinas': 4, 'grasas': 10},
    'Brownie de chocolate': {'tipo_comida': 'snack', 'calorias': 250, 'carbohidratos': 30, 'proteinas': 4, 'grasas': 12},
    'Batata asada': {'tipo_comida': 'almuerzo', 'calorias': 180, 'carbohidratos': 40, 'proteinas': 2, 'grasas': 0},
    'Pollo al curry': {'tipo_comida': 'cena', 'calorias': 400, 'carbohidratos': 50, 'proteinas': 25, 'grasas': 15},
    'Risotto de champiñones': {'tipo_comida': 'cena', 'calorias': 350, 'carbohidratos': 60, 'proteinas': 10, 'grasas': 12},
    'Falafel': {'tipo_comida': 'almuerzo', 'calorias': 300, 'carbohidratos': 40, 'proteinas': 12, 'grasas': 15},
    'Hamburguesa de ternera': {'tipo_comida': 'cena', 'calorias': 500, 'carbohidratos': 40, 'proteinas': 25, 'grasas': 25},
    'Ensalada griega': {'tipo_comida': 'almuerzo', 'calorias': 200, 'carbohidratos': 10, 'proteinas': 6, 'grasas': 15},
    'Crema de espinacas': {'tipo_comida': 'almuerzo', 'calorias': 150, 'carbohidratos': 20, 'proteinas': 5, 'grasas': 8},
    'Pasta Alfredo': {'tipo_comida': 'cena', 'calorias': 400, 'carbohidratos': 50, 'proteinas': 15, 'grasas': 20},
        
        // Agrega más datos predefinidos aquí
    };

    var nombreField = document.querySelector('input[name="nombre"]');
    var customComidaField = document.getElementById('custom-comida-field');
    var tipoComidaField = document.querySelector('select[name="tipo_comida"]');
    var caloriasField = document.querySelector('input[name="calorias"]');
    var carbohidratosField = document.querySelector('input[name="carbohidratos"]');
    var proteinasField = document.querySelector('input[name="proteinas"]');
    var grasasField = document.querySelector('input[name="grasas"]');

    $(nombreField).autocomplete({
        source: Object.keys(predefinedData),
        select: function(event, ui) {
            var selectedValue = ui.item.value;
            if (selectedValue in predefinedData) {
                var data = predefinedData[selectedValue];
                tipoComidaField.value = data.tipo_comida;
                caloriasField.value = data.calorias;
                carbohidratosField.value = data.carbohidratos;
                proteinasField.value = data.proteinas;
                grasasField.value = data.grasas;
                customComidaField.style.display = 'none';
            } else {
                customComidaField.style.display = 'block';
            }
        }
    });

    function toggleCustomComidaField() {
        if (nombreField.value === 'Personalizado') {
            customComidaField.style.display = 'block';
        } else {
            customComidaField.style.display = 'none';
        }
    }

    nombreField.addEventListener('change', toggleCustomComidaField);
    toggleCustomComidaField();  // Run on page load
});