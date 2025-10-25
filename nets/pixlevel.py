import torch
import torch.nn as nn
import torch.nn.functional as F

# Enhanced Squeeze Excitation with Leaky ReLU and adjustable negative slope
class EnhancedSqueezeExcitation(nn.Module):
    def __init__(self, in_channels, reduction=8, negative_slope=0.2):
        super(EnhancedSqueezeExcitation, self).__init__()
        self.global_avgpool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Sequential(
            nn.Linear(in_channels, in_channels // reduction, bias=False),
            nn.LeakyReLU(negative_slope=negative_slope, inplace=True),  # LeakyReLU with adjustable slope
            nn.Linear(in_channels // reduction, in_channels, bias=False),
            nn.Sigmoid()
        )

    def forward(self, x):
        b, c, _, _ = x.size()
        y = self.global_avgpool(x).view(b, c)
        y = self.fc(y).view(b, c, 1, 1)
        return x * y.expand_as(x)

# Improved Pixel-Level Module with Enhanced Squeeze Excitation and Dropout
class ImprovedPixLevelModule(nn.Module):
    def __init__(self, in_channels, reduction=16, dropout_rate=0.2, negative_slope=0.2):
        super(ImprovedPixLevelModule, self).__init__()
        self.conv_avg = nn.Conv2d(in_channels, in_channels, kernel_size=1, bias=False)
        self.conv_max = nn.Conv2d(in_channels, in_channels, kernel_size=1, bias=False)
        self.conv_out = nn.Conv2d(in_channels, in_channels, kernel_size=1, bias=True)
        self.relu = nn.ReLU(inplace=True)
        self.se_block = EnhancedSqueezeExcitation(in_channels, reduction, negative_slope)
        self.dropout = nn.Dropout(dropout_rate)  # Dropout set to 0.2 for regularization

    def forward(self, x):
        b, c, h, w = x.size()
        if c != self.conv_avg.in_channels:
            x = x.expand(b, self.conv_avg.in_channels, h, w)
        
        x_avg = self.conv_avg(x)
        x_max = self.conv_max(x)
        x_out = self.relu(x_avg + x_max)
        x_out = self.conv_out(x_out)
        
        # Apply SE block after convolution
        x_out = self.se_block(x_out)
        
        x_out = self.dropout(x_out)
        return x_out


# You can replace PixLevelModule with the ImprovedPixLevelModule class
PixLevelModule = ImprovedPixLevelModule

