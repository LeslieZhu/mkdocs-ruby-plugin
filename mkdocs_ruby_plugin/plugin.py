import re
import logging

from mkdocs.config import base, config_options as c
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.nav import Navigation
from mkdocs.structure.pages import Page
from mkdocs.utils.templates import TemplateContext



logger = logging.getLogger("mkdocs.plugins")


class RubyPluginConfig(base.Config):
    global_enable = c.Type(bool, default=True)
    title_enable = c.Type(bool, default=True)
    
    outer_begin = c.Type(str, default='{')
    outer_end = c.Type(str, default='}')
    
    inter_begin = c.Type(str, default='(')
    inter_end = c.Type(str, default=')')


class RubyPlugin(BasePlugin[RubyPluginConfig]):

    def check_ruby_disable(self, page: Page):
        # enable for single page with: meta.ruby = True
        if not self.config.global_enable and (not page.meta or not page.meta.get("ruby", False)):
            return True

        # disable for single page with: meta.ruby = False
        if self.config.global_enable and page.meta and not page.meta.get("ruby", True):
            return True

    def check_ruby_title_disable(self, page: Page):
        # enable for single page with: meta.ruby_title = True
        if not self.config.title_enable and (not page.meta or not page.meta.get("ruby_title", False)):
            return True

        # disable for single page with: meta.ruby_title = False
        if self.config.title_enable and page.meta and not page.meta.get("ruby_title", True):
            return True
        
    def on_page_content(self, html: str, *, page: Page, config: MkDocsConfig, files: Files) -> str:
        if self.check_ruby_disable(page):
            return html

        html = self.reemplazar_expresiones(html)

        if not self.check_ruby_title_disable(page):
            page.title = self.eliminar_caracteres_control(page.title)
        
        return html

    def on_page_context(self, context: TemplateContext, *, page: Page, config: MkDocsConfig,
                        nav: Navigation) -> TemplateContext:
        if self.check_ruby_disable(page):
            return context
        
        for i in page.toc.items:
            self.recorrer_hijos(i)
        return context

    def recorrer_hijos(self, item):
        item.title = self.eliminar_caracteres_control(item.title)
        for i in item.children:
            self.recorrer_hijos(i)

    def reemplazar_expresiones(self, texto: str) -> str:
        reemplazo = (r'<ruby>\1<rt>\2</rt></ruby>')
        return self.aplicar_reemplazo(reemplazo, texto)

    def eliminar_caracteres_control(self, texto: str) -> str:
        reemplazo = r'\1'
        return self.aplicar_reemplazo(reemplazo, texto)

    def aplicar_reemplazo(self, reemplazo, texto):
        # {我(wo)}是{一只猫(yizhimao)}
        busqueda = rf'\{self.config.outer_begin}(.+?)\{self.config.inter_begin}(.+?)\{self.config.inter_end}\{self.config.outer_end}'
        texto = re.sub(busqueda, reemplazo, texto)
        
        # 我(wo)是一只猫(mao)
        busqueda = rf'(.)\{self.config.inter_begin}(.+?)\{self.config.inter_end}'
        texto = re.sub(busqueda, reemplazo, texto)

        return texto
