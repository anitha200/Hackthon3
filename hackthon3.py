class Drug:
    def __init__(self, drug_id, name):
        self.drug_id = drug_id
        self.name = name
        self.status = "Manufactured"

    def update_status(self, new_status):
        valid_statuses = ["Manufactured", "Shipped", "Received"]
        if new_status in valid_statuses:
            self.status = new_status
        else:
            print(f"Invalid status: {new_status}")

    def get_status(self):
        return self.status


class PharmaSupplyChain:
    def __init__(self):
        self.drugs = {}

    def add_drug(self, drug_id, name):
        if drug_id in self.drugs:
            print(f"Drug with ID {drug_id} already exists.")
        else:
            new_drug = Drug(drug_id, name)
            self.drugs[drug_id] = new_drug
            print(f"Drug '{name}' with ID {drug_id} added to the supply chain.")

    def update_drug_status(self, drug_id, new_status):
        if drug_id in self.drugs:
            self.drugs[drug_id].update_status(new_status)
            print(f"Drug ID {drug_id} status updated to {new_status}.")
        else:
            print(f"Drug ID {drug_id} not found.")

    def get_drug_status(self, drug_id):
        if drug_id in self.drugs:
            status = self.drugs[drug_id].get_status()
            print(f"Drug ID {drug_id} is currently in status: {status}")
        else:
            print(f"Drug ID {drug_id} not found.")

    def list_all_drugs(self):
        if not self.drugs:
            print("No drugs in the supply chain.")
        else:
            for drug_id, drug in self.drugs.items():
                print(f"Drug ID: {drug_id}, Name: {drug.name}, Status: {drug.get_status()}")


# Example Usage
if __name__ == "__main__":
    pharma_chain = PharmaSupplyChain()

    # Adding drugs to the supply chain
    pharma_chain.add_drug(1, "Aspirin")
    pharma_chain.add_drug(2, "Paracetamol")
    pharma_chain.add_drug(3, "Ibuprofen")

    # Listing all drugs
    pharma_chain.list_all_drugs()

    # Updating drug statuses
    pharma_chain.update_drug_status(1, "Shipped")
    pharma_chain.update_drug_status(2, "Received")

    # Checking the status of a specific drug
    pharma_chain.get_drug_status(1)
    pharma_chain.get_drug_status(3)

    # Listing all drugs again to see the updates
    pharma_chain.list_all_drugs()
