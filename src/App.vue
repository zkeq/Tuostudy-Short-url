<template>
  <div>
    <a-card title="短链接管理" :bordered="false" class="app">
      <a-form
        ref="formRef"
        :model="shortUrlState"
        :validateOnRuleChange="false"
      >
        <!-- 短链接列表 -->
        <a-table 
          :dataSource="shortUrlItems" 
          :pagination="false"
          rowKey="key"
        >
          <a-table-column title="短链接名称" key="key">
            <template #default="{ record }">
              <a-input v-model:value="record.key" placeholder="输入短链接名称，如：vip" />
            </template>
          </a-table-column>
          <a-table-column title="目标链接" key="value" :width="600">
            <template #default="{ record }">
              <a-input v-model:value="record.decodedValue" placeholder="输入完整链接地址，如：https://example.com/path" />
            </template>
          </a-table-column>
          <a-table-column title="操作" key="action" :width="100">
            <template #default="{ record, index }">
              <a-button 
                type="danger" 
                shape="circle"
                @click="removeShortLink(index)"
              >
                <template #icon><DeleteOutlined /></template>
              </a-button>
            </template>
          </a-table-column>
        </a-table>

        <a-form-item style="margin-top: 20px;" v-if="dataLoaded">
          <a-button type="dashed" style="width: 100%" @click="addShortLink">
            <template #icon><PlusOutlined /></template>
            添加新短链接
          </a-button>
        </a-form-item>

        <a-divider />

        <a-row :gutter="24">
          <a-col :span="6">
          </a-col>
          <a-col :span="10">
            <a-form-item ref="passwordRef" label="发布密码" name="password">
              <a-input v-model:value="shortUrlState.password" type="password" placeholder="请输入发布密码" />
            </a-form-item>
          </a-col>
          <a-col :span="6">
            <a-button :loading="isLoading" type="primary" @click="handleButtonClick">
              {{ dataLoaded ? '提交' : '拉取' }}
            </a-button>
          </a-col>
        </a-row>
      </a-form>
    </a-card>
  </div>
</template>

<script setup>
import { reactive, ref, onMounted, watch } from "vue";
import { message, Card as ACard, Form as AForm, Input as AInput, Switch as ASwitch, Divider as ADivider, Button as AButton, Row as ARow, Col as ACol, Textarea as ATextarea, Table as ATable, TableColumn as ATableColumn } from "ant-design-vue";
import { 
  PlusOutlined, 
  DeleteOutlined, 
  MenuOutlined 
} from '@ant-design/icons-vue';
import draggable from 'vuedraggable';

// 状态管理
const shortUrlState = reactive({
  data: {},
  notice: {
    text: "",
    show: false
  },
  password: ""
});

// 用于拖拽排序的项目数组
const shortUrlItems = ref([]);
// 标记数据是否已加载
const dataLoaded = ref(false);

// 移除编码/解码逻辑，直接返回原始值
const decodeUrl = (url) => {
  return url || '';
};

const encodeUrl = (url) => {
  return url || '';
};

// 从对象转换为数组格式，不进行任何编码/解码
const convertToItems = (dataObj) => {
  return Object.entries(dataObj).map(([key, value]) => ({
    key,
    value,
    decodedValue: value // 直接使用原始值
  }));
};

// 从数组转换回对象格式，不进行任何编码/解码
const convertToObject = (items) => {
  const result = {};
  items.forEach(item => {
    if (item.key.trim() !== '') {
      result[item.key] = item.decodedValue || '';
    }
  });
  return result;
};

// 添加新短链接
const addShortLink = () => {
  shortUrlItems.value.push({
    key: "",
    value: "",
    decodedValue: ""
  });
};

// 删除短链接
const removeShortLink = (index) => {
  shortUrlItems.value.splice(index, 1);
};

// 验证短链接数据
const validateShortUrlItems = () => {
  const invalidItems = shortUrlItems.value.filter(
    item => !item.decodedValue?.trim() // 只验证decodedValue不为空，允许key为空
  );
  
  if (invalidItems.length > 0) {
    console.log('无效的短链接项:', invalidItems);
    return false;
  }
  return true;
};

// 加载数据
const isLoading = ref(false);

// 从本地存储中获取密码
onMounted(() => {
  const savedPassword = localStorage.getItem('shortUrlPassword');
  if (savedPassword) {
    shortUrlState.password = savedPassword;
    fetchData(); // 如果有保存的密码，自动拉取数据
  }
});

// 拉取数据函数
const fetchData = () => {
  // 验证密码
  if (!shortUrlState.password) {
    message.error("请输入密码");
    return;
  }
  
  // 保存密码到本地存储
  localStorage.setItem('shortUrlPassword', shortUrlState.password);
  
  isLoading.value = true;
  message.loading("数据加载中...", 0);
  
  fetch(`https://tuo.icodeq.com/api/admin?password=${encodeURIComponent(shortUrlState.password)}`)
    .then(response => response.json())
    .then(data => {
      isLoading.value = false;
      message.destroy();
      
      if (data.code === 200) {
        message.success("数据加载成功");
        shortUrlState.data = data.data;
        shortUrlItems.value = convertToItems(data.data);
        dataLoaded.value = true; // 标记数据已加载
      } else {
        message.error(data.message || "加载失败");
      }
    })
    .catch(error => {
      isLoading.value = false;
      message.destroy();
      message.error("数据加载失败: " + error.message);
    });
};

// 提交数据
const onSubmit = () => {
  // 验证密码
  if (!shortUrlState.password) {
    message.error("请输入密码");
    return;
  }

  // 验证所有短链接
  console.log('提交前的短链接数据:', JSON.stringify(shortUrlItems.value));
  
  if (!validateShortUrlItems()) {
    message.error("存在未填写目标链接的项，请检查");
    return;
  }

  // 组装提交数据，不进行编码
  const updatedData = convertToObject(shortUrlItems.value);
  
  const postData = {
    new_data: updatedData,
    notice: shortUrlState.notice,
    password: shortUrlState.password,
    message: "更新短链接: " + new Date().toLocaleString()
  };

  console.log('准备提交的数据:', JSON.stringify(updatedData)); // 添加日志检查提交的数据

  isLoading.value = true;

  fetch('https://tuo.icodeq.com/api/admin', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(postData)
  })
  .then(response => response.json())
  .then(result => {
    isLoading.value = false;
    if (result.code === 200) {
      message.success("提交成功，短链接已更新，2分钟上线");
      shortUrlState.data = result.data;
      shortUrlItems.value = convertToItems(result.data);
    } else {
      message.error(result.message || "提交失败");
    }
  })
  .catch(error => {
    isLoading.value = false;
    message.error("提交失败: " + error.message);
  });
};

// 处理按钮点击事件
const handleButtonClick = () => {
  if (dataLoaded.value) {
    onSubmit();
  } else {
    fetchData();
  }
};
</script>

<style scoped>
.app {
  max-width: 1200px;
  margin: 20px auto;
}

.short-link-item {
  position: relative;
  padding: 16px;
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  margin-bottom: 16px;
  background-color: #fafafa;
}

.drag-handle {
  position: absolute;
  top: 8px;
  left: 8px;
  color: #999;
  cursor: move;
  font-size: 16px;
}

.delete-btn {
  margin-top: 30px;
}
</style>