import re
import unicodedata


class CampoPosicional:
    def __init__(self, nome, valor, obrigatorio, tipo, tamanho, posicao_inicial, posicao_final):
        self.nome = nome
        self.valor = valor
        self.obrigatorio = obrigatorio
        self.tipo = tipo
        self.tamanho = tamanho
        self.posicao_inicial = posicao_inicial
        self.posicao_final = posicao_final

    def _format_alfa(self, valor):
        """ALFA: None -> '', pad direita com espaço"""
        v = "" if valor is None else str(valor)
        return v[: self.tamanho].ljust(self.tamanho, " ")

    def _format_num(self, valor):
        """NUM: None/'' -> 0, mantém apenas dígitos, pad esquerda com 0."""
        if valor is None or valor == "":
            v = "0"
        else:
            v = str(valor)
            v = re.sub(r"\D", "", v)
            if not v:
                v = "0"
        v = v[-self.tamanho :].rjust(self.tamanho, "0")
        return v

    def _sanitize_alfa(self, s: str) -> str:
        # remove acentos (Unicode)
        s = unicodedata.normalize("NFKD", s)
        s = "".join(ch for ch in s if not unicodedata.combining(ch))
        return s

    # def _format_alfa(self, valor):
    #     """ALFA: None -> '', pad direita com espaço, sem acentos."""
    #     v = "" if valor is None else str(valor)
    #     v = self._sanitize_alfa(v)
    #     return v[: self.tamanho].ljust(self.tamanho, " ")

    def exportar(self):
        """Formata e exporta o campo.
        Observação: 'CaracterFimLinha' devolve CRLF real, fora da contagem posicional.
        """
        if self.nome.lower() in ("caracterfimlinha", "caracter_fim_linha"):
            return "\r\n"

        if self.tipo == "ALFA":
            return self._format_alfa(self.valor)
        elif self.tipo == "NUM":
            return self._format_num(self.valor)
        else:
            raise ValueError(f"Tipo desconhecido: {self.tipo}")


class Registro:
    campos = []  # A list to store the fields in the record

    def _validar_layout(self):
        last_end = 0
        fim = None
        for c in self.campos:
            is_fim = c.nome.lower() in ("caracterfimlinha", "caracter_fim_linha")
            if not is_fim:
                tam_intervalo = c.posicao_final - c.posicao_inicial + 1
                assert tam_intervalo == c.tamanho, (
                    f"{self.__class__.__name__}.{c.nome}: tamanho={c.tamanho} " f"!= intervalo {c.posicao_inicial}-{c.posicao_final}"
                )
                if last_end and c.posicao_inicial != last_end + 1:
                    raise AssertionError(
                        f"{self.__class__.__name__}.{c.nome}: início {c.posicao_inicial} " f"não contíguo ao fim {last_end}"
                    )
                last_end = c.posicao_final
            else:
                fim = c
                if last_end and c.posicao_inicial != last_end + 1:
                    raise AssertionError(
                        f"{self.__class__.__name__}.{c.nome}: início {c.posicao_inicial} " f"não contíguo ao fim {last_end}"
                    )
                last_end = c.posicao_final
        if fim is None:
            raise AssertionError(f"{self.__class__.__name__}: faltou CaracterFimLinha")

    def exportar(self):
        self._validar_layout()
        return "".join(campo.exportar() for campo in self.campos)

    def __setattr__(self, name, value):
        if name != "campos" and any(c.nome == name for c in getattr(self, "campos", [])):
            for campo in self.campos:
                if campo.nome == name:
                    campo.valor = value
                    return
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if any(c.nome == name for c in getattr(self, "campos", [])):
            for campo in self.campos:
                if campo.nome == name:
                    return campo.valor
            raise AttributeError(f"Campo desconhecido: {name}")
        return super().__getattribute__(name)


class Arquivo:
    def __init__(self, registros=None):
        self.registros = list(registros or [])

    def adicionar_registro(self, registro):
        self.registros.append(registro)

    def exportar(self):
        return "".join(reg.exportar() for reg in self.registros)

    def exportar_txt(self, caminho_arquivo, encoding="utf-8"):
        with open(caminho_arquivo, "w", encoding=encoding, newline="") as f:
            f.write(self.exportar())
