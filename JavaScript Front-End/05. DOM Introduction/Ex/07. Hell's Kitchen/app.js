function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick() {

		

       
       const input = document.querySelector('#inputs textarea')
       const inputTextarea = JSON.parse(input.value);
       const bestRestaurantElement = document.querySelector('#bestRestaurant p');
       const bestRestaurantsWorkers = document.querySelector('#workers p');
       const restaurants = [];
	   

       bestRestaurantElement.textContent = '';
       bestRestaurantsWorkers.textContent = '';


       for (const text of inputTextarea) {
        	const [restaurantName, workers] = text.split(' - ');
			let currentRestaurant = restaurants.find(restaurant => restaurant.name === restaurantName);
			if (!currentRestaurant) {
					currentRestaurant = {
					'name': restaurantName,
					'workers': [],
					avgSalary: function() {
						const sumSalaries = this.workers.reduce((sum, worker) => sum + worker.salary, 0)
						const average = sumSalaries / this.workers.length;
						return average.toFixed(2)
					}
				}
			};
			
			for (const worker of workers.split(', ')) {
				const [wName, wSalary] = worker.split(' ')
				const currentWorker = {
					'name' : wName,
					'salary' : parseInt(wSalary),
					
				};
				currentRestaurant.workers.push(currentWorker);
			}
			currentRestaurant.workers.sort((a, b) => b.salary - a.salary)
			restaurants.push(currentRestaurant);
       }
	   restaurants.sort((a,b) => b.avgSalary() - a.avgSalary())

	   const bestRestaurant = restaurants[0]
	   const bestWorkerSalary = bestRestaurant.workers[0].salary.toFixed(2)

	   const sortedWorkers = bestRestaurant.workers
	   .reduce((result, worker) => {
		   result.push(`Name: ${worker.name} With Salary: ${worker.salary}`);
		   return result;
	   }, []);

		bestRestaurantElement.textContent = `Name: ${bestRestaurant.name} Average Salary: ${bestRestaurant.avgSalary()} Best Salary: ${bestWorkerSalary}`
		bestRestaurantsWorkers.textContent = sortedWorkers.join(' ');

		input.value = '';
	}	
}

