protocolo_netpro = Proto("netpro3",  "Nuestro Protocolo de programacion de redes")

version = ProtoField.int8 ("netpro3.version", "version", base.DEC)
tipo = ProtoField.int8 ("netpro3.tipo", "tipo", base.DEC)
comando = ProtoField.int8 ("netpro3.comando", "comando", base.DEC)
estado = ProtoField.int8 ("netpro3.estado", "estado", base.DEC)
data = ProtoField.string ("netpro3.data", "data", base.ASCII)

protocolo_netpro.fields = {version, tipo, comando, estado, data}

function protocolo_netpro.dissector(buffer, pinfo, tree)
	length = buffer:len()
  	if length == 0 then return end

  	pinfo.cols.protocol = protocolo_netpro.name

  	local subtree = tree:add(protocolo_netpro, buffer(), "Data del NetPro3")
  	subtree:add(version, buffer(0,1))
  	local tipo_val = buffer(1,1):le_int()
  	local texto_tipo = "DESCONOCIDO"
  	if tipo_val == 1 then
  		texto_tipo = "PETICION"
  	elseif tipo_val == 2 then
  		texto_tipo = "RESPUESTA"
  	end
  	subtree:add(tipo, buffer(1,1)):append_text(" (" .. texto_tipo .. ") ")
  	if tipo_val == 1 then  -- Peticion
	  	local comando_val = buffer(2,1):le_int()
	  	subtree:add(comando, buffer(2,1)):append_text(" (" .. obten_texto_comando(comando_val) .. ") ")
	elseif tipo_val == 2 then -- Respuesta
		local estado_val = buffer(2,1):le_int()
	  	subtree:add(estado, buffer(2,1)):append_text(" (" .. obten_texto_estado(estado_val) .. ") ")
	end	
	subtree:add(data, buffer(3,length - 3))
end

function obten_texto_comando( comando )
	local texto = "DESCONOCIDO"
	if comando == 1 then
		texto = "FECHA"
	elseif	comando == 2 then
		texto = "INVERSO"
	elseif comando == 3 then
		texto = "DESCARGA"
	end
	return texto
end

function obten_texto_estado( estado )
	local texto = "DESCONOCIDO"
	if estado == 1 then
		texto = "EXITO"
	elseif	estado == 2 then
		texto = "FALLO"
	end
	return texto
end

local tcp_port = DissectorTable.get("tcp.port")
tcp_port:add(2224, protocolo_netpro)
