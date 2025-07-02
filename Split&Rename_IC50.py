import os
from rdkit import Chem

def split_sdf_by_ic50(input_sdf, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read molecules from the SDF file
    suppl = Chem.SDMolSupplier(input_sdf)
    count = 0

    for idx, mol in enumerate(suppl):
        if mol is None:
            continue  # skip invalid molecules

        # Get the IC50 property
        try:
            ic50_str = mol.GetProp('IC50 (nM)')
            ic50 = float(ic50_str)
        except KeyError:
            print(f"Warning: Molecule {idx} missing 'Experimental IC50' property, skipping.")
            continue
        except ValueError:
            print(f"Warning: Molecule {idx} has non-numeric IC50 value '{ic50_str}', skipping.")
            continue

        # Apply the filtering logic
        if ic50 < 150 or (10000 < ic50 < 60000):
            # Write this molecule to its own SDF file
            out_path = os.path.join(output_dir, f"mol_{idx+1}_IC50_{int(ic50)}.sdf")
            writer = Chem.SDWriter(out_path)
            writer.write(mol)
            writer.close()
            count += 1

    print(f"Done. {count} molecules written to '{output_dir}'.")

# Example usage:
# split_sdf_by_ic50('input.sdf', '/path/to/output_dir')
if __name__ == "__main__":
    input_sdf = "/Users/prathamdhanoa/Downloads/Docking/VS_Config/Validation_ROC/P.Aeruginosa_592.sdf"  # Replace with your input SDF file
    output_dir = "/Users/prathamdhanoa/Downloads/Docking/VS_Config/Validation_ROC/test_inactives_592.sdf"  # Replace with your desired output directory
    split_sdf_by_ic50(input_sdf, output_dir)
