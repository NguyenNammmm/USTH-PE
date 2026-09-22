from abc import ABC,abstractmethod
class Exporter(ABC):
    @abstractmethod
    def export(self,rows): pass
class TextExporter(Exporter):
    def export(self,rows): return ",".join(rows)
class UpperMixin:
    def export(self,rows): return super().export(rows).upper()
class LoudExporter(UpperMixin,TextExporter): pass
