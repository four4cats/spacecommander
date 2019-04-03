#import @"XYZGeometry.h"

@implementation ProblemChild	

- (void)testDict {
    NSDictionary *param = @{@"thumb": thumb,
                             @"tagids": @"",
                             @"airtime": @(0),
                             @"title": title,
                             @"gameid": @(gameId),
                             @"sdk_type": @(sdkType),
                             @"a": [a b] };

    NSError *error = [NSError errorWithDomain:NSCocoaErrorDomain code:0 userInfo:@{NSLocalizedDescriptionKey: @"stop",
                                                                                    NSLocalizedFailureReasonErrorKey: errString}];

    NSError *error = [NSError errorWithDomain:NSCocoaErrorDomain code:0 userInfo:@{NSLocalizedDescriptionKey: @"stop",
                    NSLocalizedFailureReasonErrorKey: LANG(@"common_net_connect_error") }];
}

@end
