from .exportador import Arquivo
from .exportador import CampoPosicional
from .exportador import Registro


class RPS(Arquivo):
    pass


class RegistroTipo1(Registro):
    campos = [
        CampoPosicional("TipoRegistro", "1", True, "NUM", 1, 1, 1),
        CampoPosicional("InscricaoContribuinte", None, True, "ALFA", 7, 2, 8),
        CampoPosicional("InicioPeriodo", None, False, "NUM", 8, 9, 16),
        CampoPosicional("TerminoPeriodo", None, False, "NUM", 8, 17, 24),
        CampoPosicional("VersaoLayout", "PMB002", True, "ALFA", 6, 25, 30),
        CampoPosicional("IdentificacaoRemessaContribuinte", None, False, "NUM", 11, 31, 41),
        CampoPosicional("CaracterFimLinha", "\r", True, "ALFA", 1, 42, 42),
    ]


class RegistroTipo2(Registro):
    campos = [
        CampoPosicional("TipoRegistro", "2", True, "NUM", 1, 1, 1),
        CampoPosicional("SerieNFe", None, True, "ALFA", 5, 2, 6),
        CampoPosicional("NumeroNFe", None, True, "NUM", 6, 7, 12),
        CampoPosicional("DataNFe", None, True, "NUM", 8, 13, 20),
        CampoPosicional("HoraNFe", None, True, "NUM", 6, 21, 26),
        CampoPosicional("CodigoAutenticidade", None, True, "ALFA", 24, 27, 50),
        CampoPosicional("SerieRPS", None, True, "ALFA", 4, 51, 54),
        CampoPosicional("NumeroRPS", None, True, "NUM", 10, 55, 64),
        CampoPosicional("Tributacao", None, True, "NUM", 1, 65, 65),
        CampoPosicional("ISSRetido", None, True, "ALFA", 1, 66, 66),
        CampoPosicional("SituacaoNFe", None, True, "ALFA", 1, 67, 67),
        CampoPosicional("DataCancelamento", None, False, "NUM", 8, 68, 75),
        CampoPosicional("NumeroGuia", None, False, "NUM", 10, 76, 85),
        CampoPosicional("DataPagamentoGuia", None, False, "NUM", 8, 86, 93),
        CampoPosicional("CPFCNPJTomador", None, True, "NUM", 14, 94, 107),
        CampoPosicional("RazaoSocialNomeTomador", None, True, "ALFA", 100, 108, 207),
        CampoPosicional("EnderecoLogradouroTomador", None, True, "ALFA", 100, 208, 307),
        CampoPosicional("NumeroLogradouroTomador", None, True, "ALFA", 9, 308, 316),
        CampoPosicional("ComplementoLogradouroTomador", None, False, "ALFA", 20, 317, 336),
        CampoPosicional("BairroLogradouroTomador", None, True, "ALFA", 40, 337, 376),
        CampoPosicional("CidadeLogradouroTomador", None, True, "ALFA", 40, 377, 416),
        CampoPosicional("UFLogradouroTomador", None, True, "ALFA", 2, 417, 418),
        CampoPosicional("CEPLogradouroTomador", None, True, "ALFA", 8, 419, 426),
        CampoPosicional("PaisLogradouroTomador", None, False, "ALFA", 50, 427, 476),
        CampoPosicional("EmailTomador", None, False, "ALFA", 152, 477, 628),
        CampoPosicional("DiscriminacaoServico", None, True, "ALFA", 1000, 629, 1628),
        CampoPosicional("CaracterFimLinha", "\r", True, "ALFA", 1, 1629, 1629),
    ]


class RegistroTipo3(Registro):
    campos = [
        CampoPosicional("TipoRegistro", "3", True, "NUM", 1, 1, 1),
        CampoPosicional("QuantidadeServico", None, True, "NUM", 6, 2, 7),
        CampoPosicional("DescricaoServico", None, True, "ALFA", 60, 8, 67),
        CampoPosicional("CodigoServico", None, True, "NUM", 9, 68, 76),
        CampoPosicional("ValorUnitarioServico", None, True, "NUM", 15, 77, 91),
        CampoPosicional("AliquotaServico", None, True, "NUM", 4, 92, 95),
        CampoPosicional("CaracterFimLinha", "\r", True, "ALFA", 1, 96, 96),
    ]


class RegistroTipo4(Registro):
    campos = [
        CampoPosicional("TipoRegistro", "4", True, "NUM", 1, 1, 1),
        CampoPosicional("CodigoOutrosValores", None, True, "ALFA", 2, 2, 3),
        CampoPosicional("Valor", None, True, "NUM", 15, 4, 18),
        CampoPosicional("CaracterFimLinha", "\r", True, "ALFA", 1, 19, 19),
    ]


class RegistroTipo9(Registro):
    campos = [
        CampoPosicional("TipoRegistro", "9", True, "NUM", 1, 1, 1),
        CampoPosicional("NumeroTotalLinhas", None, True, "NUM", 7, 2, 8),
        CampoPosicional("ValorTotalServicos", None, True, "NUM", 15, 9, 23),
        CampoPosicional("ValorTotalValores", None, True, "NUM", 15, 24, 38),
        CampoPosicional("CaracterFimLinha", "\r", True, "ALFA", 1, 39, 39),
    ]
