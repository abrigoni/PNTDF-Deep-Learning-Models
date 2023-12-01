import torch

# Verifica si CUDA (GPU) está disponible
if torch.cuda.is_available():
    # Obtiene el nombre de la GPU
    gpu_name = torch.cuda.get_device_name(0)  # 0 representa el primer dispositivo GPU

    print(f"Nombre de la GPU: {gpu_name}")
else:
    print("CUDA no está disponible. Verifica tu configuración de GPU.")

