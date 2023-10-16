const gridSize = 10;
		const mineCount = 10;
		 grid = document.getElementById("grid");

		// Generate random mines using maths.random function
		const mines = Array.from({ length: gridSize * gridSize }, () => Math.random() < 0.2);

		// create 10X10 table
		for (let i = 0; i < gridSize * gridSize; i++) {
			const cell = document.createElement("div");
			cell.className = "cell";

			grid.appendChild(cell);

			// Handles cell click event
			cell.addEventListener("click", () => {
				if (mines[i]) {
					cell.style.backgroundColor = "red";
					alert("You are bombed! try again");
					window.location.reload();
				} else {
					const count = getAdjacentMinesCount(i);
					cell.textContent = count;
				}
			});
		}

		// Get count of adjacent mines
		function getAdjacentMinesCount(index) {
		    //find position of the cell
			const positions = [-gridSize - 1, -gridSize, -gridSize + 1, -1, 1, gridSize - 1, gridSize, gridSize + 1];

			let count = 0;
			//count the no of bombs adjacent to cell
			for (const offset of positions) {
				const newIndex = index + offset;
				if (mines[newIndex]!== undefined && mines[newIndex]) {
					count++;
				}
			}
			return count;
		}