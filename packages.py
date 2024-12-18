import argostranslate.package
from tqdm import tqdm

def install_packages():
    argostranslate.package.update_package_index()
    
    pkgs = available_uninstalled()
    if not pkgs:
        # no new packages to add
        return

    print("Installing translation packages. If this keep happening with every run, add the `-n` flag.")
    for pkg in tqdm(pkgs):
            argostranslate.package.install_from_path(pkg.download())

def update_packages():
    installed = argostranslate.package.get_installed_packages()

    print("Updating installed translation packages")
    for package in tqdm(installed):
        package.update()

def available_uninstalled():
    already_installed = set(map(lambda pkg: (pkg.from_code, pkg.to_code), argostranslate.package.get_installed_packages()))
    available_packages = argostranslate.package.get_available_packages()

    output = []
    for pkg in available_packages:
        if (pkg.from_code, pkg.to_code) not in already_installed:
            output.append(pkg)
    return output