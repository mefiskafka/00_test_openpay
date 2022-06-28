READ_CSV_CONFIGS = {
    'columns': {
        "Comercio Id": "comercio_id", 
        "Mes Operacion": "mes_operacion", 
        "Estado": "estado",
        "Moneda": "moneda",
        "# Transacciones": "num_transacciones",
        "Monto Transaccion": "monto_transaccion",
        "Monto Contracargo (Venta)": "monto_contracargo_venta",
    },
    'cast': {
        "comercio_id": "int",
        "num_transacciones": "int64", 
        "monto_transaccion": "int64", 
        "monto_contracargo_venta": "int64"
    }
}
