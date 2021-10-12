# Maintainer: TeddyOwO <teddyuwu {at] protonmail {dot} com>
pkgname=awm-git
_pkgname=awm
pkgver=r1.62bd9b0
pkgrel=1
epoch=1
pkgdesc="Historical Arch Linux packages downloader."
arch=('any')
url="https://github.com/AlphaNecron/${_pkgname}"
license=('ISC')
provides=($_pkgname)
conflicts=($_pkgname)
makedepends=('git')
source=("git+https://github.com/AlphaNecron/arch_wayback_machine.git")
md5sums=('SKIP')

pkgver() {
  cd $_pkgname
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  cd $_pkgname
  install -D -m755 awm "${pkgdir}/usr/bin/${_pkgname}"
}
