{
  outputs = { nixpkgs, ... }:
    let
      pkgs = import nixpkgs {
        system = "x86_64-linux";
      };
      python-env = pkgs.python3Full.withPackages (ps: with ps; [
        customtkinter
        pyserial
        toml
        requests
        mypy
        ruff
        types-requests
        types-toml
      ]);
    in {
      devShell.x86_64-linux = pkgs.mkShell {
        buildInputs = with pkgs; [
          python-env
        ];
      };
    };
}
