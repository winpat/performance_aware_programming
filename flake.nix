{
  description = "My personal playground for Casey Muratori's Computer, Enhance! course.";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-22.11";
  };

  outputs = { self, nixpkgs }:
    let pkgs = nixpkgs.legacyPackages.x86_64-linux;
        deps = [
          pkgs.just
          pkgs.python3
          pkgs.python3Packages.pytest
          pkgs.python3Packages.pytest-benchmark
          pkgs.python3Packages.pytest-isort
          pkgs.python3Packages.pytest-flake8
          pkgs.python3Packages.pytest-black
          pkgs.python3Packages.pytest-mypy
          pkgs.python3Packages.ipdb
        ];
    in {
      devShell.x86_64-linux = pkgs.mkShell {
        buildInputs = deps;
      };
    };
}
