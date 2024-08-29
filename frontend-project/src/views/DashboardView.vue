<script setup lang="ts">
import Sidebar from '../components/Dashboard/sidebar.vue';
import Topbar from '../components/Dashboard/Topbar.vue';
import BlankPage from '../components/Dashboard/BlankPage.vue';
import FooterCom from '../components/Dashboard/FooterCom.vue';
</script>


<template>
 <!-- Page Wrapper -->
 <div id="wrapper">

<Sidebar></Sidebar>
<!-- Content Wrapper -->
<div id="content-wrapper" class="d-flex flex-column">

    <!-- Main Content -->
    <div id="content">

      <Topbar></Topbar>
      <BlankPage></BlankPage>
   
    </div>
    <!-- End of Main Content -->

  <FooterCom></FooterCom>

</div>
<!-- End of Content Wrapper -->

</div>
<!-- End of Page Wrapper -->
</template>
