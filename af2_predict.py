
# Jobname for reference
jobname = '1ake'

# Amino acid sequence. Whitespace and inappropriate characters are automatically removed
sequence = ("MRIILLGAPGAGKGTQAQFIMEKYGIPQISTGDMLRAAVKSGSELGKQAKDIMDAGKLVTDELVIALVKERIAQEDCRNGFLLDGFPRTIPQADAMKEAGINVDYVLEFDVPDELIVDRIVGRRVHAPSGRVYHVKFNPPKVEGKDDVTGEELTTRKDDQEETVRKRLVEYHQMTAPLIGYYSKEAEAGNTKYAKVDGTKPVAEVRADLEKILG")
            
from scripts import predict

msa_file_path = "./1ake_out/1AKE_A.a3m"
with open(msa_file_path, 'r') as file:
        a3m_lines = file.read()

print("a3m lines",len(a3m_lines))
print("a3m lines first 200",a3m_lines[:200])


predict.predict_structure_no_templates( sequence, "./1ake_out/out.pdb",
         a3m_lines, model_id = 1, max_msa_clusters = 16,
         max_extra_msa = 32, max_recycles = 1, n_struct_module_repeats = 8 )