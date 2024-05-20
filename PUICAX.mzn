int: n_clientes;
int: n_sitios;
array[1..n_sitios] of float: costo_fijo_sitios;
array[1..n_sitios] of int: capacidad_maxima_sitios;
array[1..n_clientes] of float: demanda_clientes;
array[1..n_clientes, 1..n_sitios] of float: beneficio_por_unidad;


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