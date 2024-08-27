<template>
 <div>
  <p>{{ message }}</p>
  <button @click="updateMessage">Actualizar mensaje</button>
</div>
</template>




<script>



import { ref } from 'vue';
 
 export default {
   setup() {
     const message = ref('Hola Vue 3');
 
     const updateMessage = () => {
       message.value = '¡Mensaje actualizado!';
     };
 
     return { message, updateMessage };
   }
 }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
