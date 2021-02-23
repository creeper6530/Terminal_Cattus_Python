# Návody

### Hlavní menu:
<style>nav ul {list-style-type:none;background-color:#b3b3b3;border: 4px solid #111111;border-radius: 10px;font-family:sans-serif;font-weight:bold;padding: 16px;}nav ul li {display:inline;border-right: 2px solid #111111;padding-right: 8px;padding-left: 8px;}</style>

<nav>
<ul>
<li><a href="index.html">Hlavní stránka</a></li>
<li><a href="pomoc.html">Pomoc</a></li>
</ul>
</nav>

Vítejte na stránce pro návody. Najdete zde všechny potřebné návody pro terminál Cattus.   
> Tyto návody jsou vytvořeny tvůrcem exkluzivně pro tento web.

## Instalace terminálu na počítač bez Pythonu

1. Stáhněte si kompilovaný terminál z GitHubu ze záložky Releases.
1. Přesuňte stažený `.exe` soubor do umístění, kde ho můžete jednoduše spustit.
1. Spusťte stažený `.exe` soubor.
1. Pokud bude program zachycen antivirovým programem, ignorujte to.
> Malé okénko: Hodně antivirů bude tento program zachytávat jako nebezpečný, protože program není digitálně podepsaný. Ale kvůli tomu, že to kompiluji programem PyInstaller, tak pro mě není možné to podepisovat.
> 
> Pokud bude program zachycen antiransomwarovým programem, můžete to taky ignorovat, protože program má sám do sebe zabalené všechny moduly, na kterých je závislý a které musí sám ze sebe extrahovat, a těch je hodně. Ale díky tomu je jednodušší se v zdrojovém kódu orientovat.
> 
> Pokud nevěříte tomu, co jsem vám teď řekl, nevím, proč si čtete tento návod. Předpokládám, že když mi nevěříte, tak si to instalovat nebudete ;-)

## Umožnění spuštění terminálu z `cmd.exe` nebo z Powershellu nezávisle na umístění, ve kterém umístění tyto terminály pracují

1. Nainstalujte terminál podle návodu na této stránce.
1. Přesuňte stažený `.exe` soubor do složky `C:\Windows`
> Malé okénko: Přesouváte to do té složky proto, aby jste ten `.exe` soubor měli v globální proměnné `PATH`.
> 
> V tomto návodu jsem se inspiroval jiným návodem, který jsem si ozkoušel.
> 
> Více o globální proměnné `PATH` vám řekne odbornější stránka.
1. Spusťte `cmd.exe` nebo Powershell a zadejte do něj název `.exe` souboru (bez přípony).
