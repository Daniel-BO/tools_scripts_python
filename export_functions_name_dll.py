import pefile

# Load the DLL
pe = pefile.PE("file.dll")

# Print all exported functions
if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
    print("[*] Exported functions:")
    with open("exported_functions.txt", "w") as file_txt:
	    for symbol in pe.DIRECTORY_ENTRY_EXPORT.symbols:
	        if symbol.name:
	         print(symbol.name.decode("utf-8"), file=file_txt)
            
else:
    print("[-] No exports found in the DLL.")
