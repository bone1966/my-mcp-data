import csv

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Sales MCP server")


@mcp.tool()
def get_sales_from_customer(customer_name: str) -> list[int]:
    """Get a list of all sales totals for a given customer."""
    sales: list[int] = []
    with open("data/sales.csv", "r") as f:
        reader = csv.reader(f)
        for name, paid in reader:
            if name == customer_name:
                sales.append(int(paid))
        return sales
    
    
if __name__ == "__main__":
    mcp.run()
