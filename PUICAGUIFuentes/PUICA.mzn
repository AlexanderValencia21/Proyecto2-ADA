include "PUICAX.dzn";
output ["n_clientes: ", show(n_clientes), "\n"];
output ["n_sitios: ", show(n_sitios), "\n"];
output ["costo_fijo_sitios: ", show(costo_fijo_sitios), "\n"];
output ["capacidad_maxima_sitios: ", show(capacidad_maxima_sitios), "\n"];
output ["demanda_clientes: ", show(demanda_clientes), "\n"];
output ["beneficio_por_unidad: ", show(beneficio_por_unidad), "\n"];





array[1..n_clientes, 1..n_sitios] of var float: productos;

array[1..n_sitios] of var bool: instalaciones;





constraint forall(c in 1..n_clientes, s in 1..n_sitios)(productos[c,s] >= 0);

constraint forall(c in 1..n_clientes)((sum(s in 1..n_sitios)(productos[c,s])) == demanda_clientes[c]);

constraint forall(s in 1..n_sitios)((sum(c in 1..n_clientes)(productos[c,s])) <= capacidad_maxima_sitios[s]*instalaciones[s]);





var float: beneficio_total;
constraint beneficio_total = sum(c in 1..n_clientes, s in 1..n_sitios)(beneficio_por_unidad[c,s]*productos[c,s]);
var float: costo_total_fijo_sitios;
constraint costo_total_fijo_sitios = sum(s in 1..n_sitios)(costo_fijo_sitios[s]*instalaciones[s]);

var float: utilidad_total;
constraint utilidad_total = beneficio_total - costo_total_fijo_sitios;





solve maximize utilidad_total;





output ["utilidad_total: ", show(utilidad_total), "\n"];
output ["instalaciones: ", show(instalaciones), "\n"];
output ["productos: ", show(productos), "\n"];
