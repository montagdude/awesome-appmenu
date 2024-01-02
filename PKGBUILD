pkgname="Shared-AwesomeAppMenu"
pkgver="1.0"
pkgrel="1"
pkgdesc="A Python tool to display the applications menu on the standard Awesome Bar"

arch=('any')
url="https://github.com/sharedordaz/Shared-AwesomeAppMenu"
licence=('GPL3')
depends=("python" "adwaita-icon-theme" "awesome")
makedepends=("git" )

source=("${url}/archive/refs/tags/${pkgver}.tar.gz")

md5sums=("SKIP")
build() {
    return 0   
}

package(){

cd "${srcdir}/${pkgname}-${pkgver}"

#chmod +w /usr/share/
    	
make DESTDIR="pkgdir" install

}


