<template>
	<v-container fluid grid-list-md>
    <v-layout column>
      		<v-card flat class="machine-main-card">
      			<v-toolbar flat class="result-toolbar">
      				<v-toolbar-title class="result-toolbar"> 
      					Postgres history page: {{ alias }} 
      				</v-toolbar-title>
      				<v-spacer></v-spacer>
            		<v-btn class="login-button" :href="'/machine/'+ id"> View history </v-btn>
            	</v-toolbar>
        	<v-layout row>
        	<v-flex>
        	<v-card flat>
		        <v-card-text class="machine-main-text">
		          Machine type: {{ type }} <br>
		          Kernel: {{ kernel }}
		        </v-card-text>
		    </v-card>
		</v-flex>
		<v-flex>
		    <v-card flat>
		        <v-card-text class="machine-main-text">
		          First run: <u> <router-link :to="{path: '/run/' + first_run }"> {{ first_run }} </router-link> </u> <br>
		          First run: <u> <router-link :to="{path: '/run/' + last_run }"> {{ last_run }} </router-link> </u> <br>
		        </v-card-text>
		    </v-card>
		</v-flex>
		<v-flex>
		    <v-card flat>
		        <v-card-text class="machine-main-text">
		          First run date: {{ first_run_date }} <br>
		          Last run date: {{ last_run_date }}
		        </v-card-text>
		    </v-card>
		</v-flex>
         </v-layout>
     
     </v-card>
    
      
      <v-flex>
          	<v-card flat class="profile-card-title-postgres">
          		<v-tabs
					v-model="tab"
					  class="tabs"
				>
					<v-tabs-slider color="white"></v-tabs-slider>
					<v-tab v-for="(value, name) in postgres_history" :key="name"> <span style="color: white"> {{ name }} </span> </v-tab>
				</v-tabs>
					
					<v-tabs-items v-model="tab" class="tabs-div">
						<v-tab-item v-for="(value, name) in postgres_history" :key="name">
							<v-card flat>	
								<v-card-text>
		                    		<table class="mounts-center">
		                    			<tr class="mounts-r">
										    		<th class="mounts-h"> <b> First run </b> </th>
										    		<th class="mounts-h"> <b> Edit date </b> </th>
										    		<th class="mounts-h"> <b> Setting name </b> </th>
										    		<th class="mounts-h"> <b> Setting unit (previous) </b> </th>
										    		<th class="mounts-h"> <b> Setting unit (next) </b> </th>
										    		<th class="mounts-h"> <b> Setting value (previous) </b> </th>
										    		<th class="mounts-h"> <b> Setting value (next) </b> </th>
										  </tr> 
										  		<tr v-for="item in value" :key="item.run_id" class="mounts-r">
													<td class="mounts-d"> <u> <router-link :to="{path: '/run/' + item.run_id }"> {{ item.run_id }} </router-link> </u> <br> </td>
													<td class="mounts-d"> {{ item.add_time }} </td>
													<td class="mounts-d"> {{ item.setting_name }} </td>
													<td class="mounts-d"> {{ item.unit1 }} </td>
													<td class="mounts-d"> {{ item.unit2 }} </td>
													<td class="mounts-d"> {{ item.value1 }} </td>
													<td class="mounts-d"> {{ item.value2 }} </td> 
												   
										  		</tr> 
		                    		</table>
		                    	</v-card-text>
							</v-card>
						</v-tab-item>
					</v-tabs-items>

          	</v-card>
      	</v-flex>
    
  </v-layout>
  </v-container>
	

</template>

<script>

	export default {
		name: 'Postgres',

		data: () => ({

			tab: null,
	  		
	  		alias: '',
	  		id: '',
	  		type: '',
	  		kernel: '',
	  		first_run: '',
	  		first_run_date: '',
	  		last_run: '',
	  		last_run_date: '',
	  		postgres_history: {},

		}),

		methods: {

			getPostgres() {

				var url = this.$store.state.endpoints.postgres + this.$route.params.id;

				const httpRequest = new XMLHttpRequest();
				httpRequest.open("GET", url);
				httpRequest.send();

				httpRequest.onreadystatechange = () => {

			  		if (httpRequest.readyState === XMLHttpRequest.DONE) {

						if (httpRequest.status === 200) {
				  			var response = JSON.parse(httpRequest.response);

				  			this.alias = response[0].alias;
				  			this.id = response[0].machine_id;
				  			this.kernel = response[0].kernel_name;
				  			this.type = response[0].machine_type;
				  			this.first_run = response[0].first_run;
				  			this.last_run = response[0].last_run;
				  			this.first_run_date = new Date(response[0].min_add_time);
				  			this.last_run_date = new Date(response[0].max_add_time);

				  			for (let i = 0; i < response.length; i++) {

				  				var set = {'run_id': response[i].min, 'setting_name': response[i].setting_name, 'unit1': response[i].unit1, 'unit2': response[i].unit2, 'value1': response[i].value1, 'value2': response[i].value2, 'add_time': response[i].add_time.substring(0, 10)};

				  				if (!this.postgres_history.hasOwnProperty(response[i].name)) {
									this.postgres_history[response[i].name] = [];
								}

								this.postgres_history[response[i].name].push(set);

				  			}

				  			console.log(this.postgres_history);
			
				  		}
				  	}
				  	else {
						console.log(httpRequest.status);
					}
				}
		  	}
		},

		mounted() {
			this.getPostgres();
		}
  	}

</script>