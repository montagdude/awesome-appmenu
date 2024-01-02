pkgname="awesome-appmenu"
pkgver="0.1"
pkgrel="1"
pkgdesc="A tool to create a menu of installed applications on the awesome default bar"

arch=('any')
url="https://github.com/sharedordaz/awesome-appmenu"
licence=('GPL-3.0')
depends=("python" "adwaita-icon-theme" "awesome")
makedepends=("git" )

source=("${url}/archive/v${pkgver}.tar.gz")
#source=("${pkgname}"
#        "Makefile"
#        "README.md"
#        "LICENSE"
#        "awesome-appmenu.png"
#        "menurc.py"
#        "menurc.pyc")

md5sums=("SKIP")
build() (return 0)

package()(

#cd "${srcdir}/${pkgname}-${pkgver}.tar.gz"

#chmod +w /usr/share/
    	
make DESTDIR="pkgdir" install


)


